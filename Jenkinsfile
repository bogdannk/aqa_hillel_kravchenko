pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
        REPORT_DIR = 'lesson_30/reports'
        REPORT_FILE = 'report.xml'
    }

    stages {
        stage('Installing Python') {
            steps {
                script {
                    sh """
                        if [ -d "\$HOME/.pyenv" ]; then
                            echo "Python already exists. Removing existing pyenv installation..."
                            rm -rf \$HOME/.pyenv
                        fi

                        echo "Installing pyenv..."
                        curl https://pyenv.run | bash

                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"

                        echo "Installing Python version ${PYTHON_VERSION}..."
                        pyenv install ${PYTHON_VERSION}
                        pyenv global ${PYTHON_VERSION}
                    """
                }
            }
        }

        stage("Creation of Python virtual environment") {
            steps {
                script {
                    sh """
                        if [ ! -d "${VENV_DIR}" ]; then
                            echo "Creating virtual environment..."
                            python3 -m venv ${VENV_DIR}
                        else
                            echo "Virtual environment already exists."
                        fi
                    """
                }
            }
        }

        stage("Activating venv, installing dependencies, and executing test cases") {
            steps {
                script {
                    sh """
                        source ${VENV_DIR}/bin/activate

                        echo "Upgrading pip..."
                        pip install --upgrade pip
                        echo "Installing dependencies from requirements.txt..."
                        pip install -r requirements.txt

                        # Создаём папку для отчётов
                        mkdir -p ${REPORT_DIR}

                        echo "Running tests and generating report..."
                        pytest --maxfail=1 --disable-warnings -q --junitxml=${REPORT_DIR}/${REPORT_FILE} lesson_30/test_initial.py
                    """
                }
            }
        }

        stage("Publish Test Results") {
            steps {
                junit "${REPORT_DIR}/${REPORT_FILE}"
            }
        }
    }
}
