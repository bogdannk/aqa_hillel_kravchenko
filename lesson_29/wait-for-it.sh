#!/usr/bin/env bash

WAITFORIT_cmdname=${0##*/}

usage() {
    echo "Usage:"
    echo "    $WAITFORIT_cmdname host:port [-s] [-t timeout] [-- command args]"
    echo "    -h HOST | --host=HOST       Host or IP to check"
    echo "    -p PORT | --port=PORT       TCP port to check"
    echo "                                Or specify host and port in the format host:port"
    echo "    -s | --strict               Only execute the command if the check is successful"
    echo "    -q | --quiet                Do not output any status messages"
    echo "    -t TIMEOUT | --timeout=TIMEOUT Timeout in seconds, 0 - no timeout"
    echo "    -- COMMAND ARGS             Execute command with args after the check completes"
    exit 1
}

wait_for() {
    local start_ts=$(date +%s)
    echoerr "$WAITFORIT_cmdname: waiting for $WAITFORIT_HOST:$WAITFORIT_PORT"
    while ! (echo -n > /dev/tcp/$WAITFORIT_HOST/$WAITFORIT_PORT) >/dev/null 2>&1; do
        sleep 1
    done
    echoerr "$WAITFORIT_cmdname: $WAITFORIT_HOST:$WAITFORIT_PORT is available after $(( $(date +%s) - start_ts )) seconds"
}

echoerr() { [[ $WAITFORIT_QUIET -ne 1 ]] && echo "$@" 1>&2; }

# Argument processing
while [[ $# -gt 0 ]]; do
    case "$1" in
        *:*) IFS=':' read -r WAITFORIT_HOST WAITFORIT_PORT <<< "$1"; shift ;;
        -h) WAITFORIT_HOST="$2"; shift 2 ;;
        -p) WAITFORIT_PORT="$2"; shift 2 ;;
        -t) WAITFORIT_TIMEOUT="$2"; shift 2 ;;
        -q) WAITFORIT_QUIET=1; shift ;;
        -s) WAITFORIT_STRICT=1; shift ;;
        --) shift; WAITFORIT_CLI=("$@"); break ;;
        --help) usage ;;
        *) echoerr "Unknown argument: $1"; usage ;;
    esac
done

[[ -z "$WAITFORIT_HOST" || -z "$WAITFORIT_PORT" ]] && { echoerr "Error: host and port must be specified for checking."; usage; }

WAITFORIT_TIMEOUT=${WAITFORIT_TIMEOUT:-15}
WAITFORIT_QUIET=${WAITFORIT_QUIET:-0}

wait_for

if [[ "${WAITFORIT_CLI[@]}" ]]; then
    [[ $WAITFORIT_RESULT -ne 0 && $WAITFORIT_STRICT -eq 1 ]] && { echoerr "$WAITFORIT_cmdname: strict mode, refusing to execute subprocess"; exit $WAITFORIT_RESULT; }
    exec "${WAITFORIT_CLI[@]}"
else
    exit 0
fi