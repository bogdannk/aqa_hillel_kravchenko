pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
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
                        if [ ! -d "\${VENV_DIR}" ]; then
                            echo "Creating virtual environment..."
                            python -m venv \${VENV_DIR}
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

                        echo "Running tests..."
                        pytest --maxfail=1 --disable-warnings -q lesson_30/test_initial.py
                    """
                }
            }
        }
    }
}