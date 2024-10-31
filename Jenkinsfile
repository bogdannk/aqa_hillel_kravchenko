pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/bogdannk/aqa_hillel_kravchenko.git', branch: 'main'
            }
        }

        stage('Install Python with pyenv') {
            steps {
                script {
                    sh """
                        if [ -d "\$HOME/.pyenv" ]; then
                            echo "Pyenv is already installed."
                        else
                            echo "Installing pyenv..."
                            curl https://pyenv.run | bash
                            export PATH="\$HOME/.pyenv/bin:\$PATH"
                            eval "\$(pyenv init --path)"
                            eval "\$(pyenv init -)"
                            pyenv install ${PYTHON_VERSION}
                            pyenv global ${PYTHON_VERSION}
                        fi
                        # Обновляем PATH и инициализируем pyenv
                        export PATH="\$HOME/.pyenv/bin:\$PATH"
                        eval "\$(pyenv init --path)"
                        eval "\$(pyenv init -)"
                    """
                }
            }
        }

        stage('Create Python Virtual Environment') {
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

        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                        # Активация виртуального окружения и установка зависимостей
                        source ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh """
                        # Активация виртуального окружения и запуск тестов
                        source ${VENV_DIR}/bin/activate
                        pytest --maxfail=1 --disable-warnings -q tests/
                    """
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit '**/test-*.xml' // Предполагается, что результаты тестов в формате JUnit XML
            }
        }
    }

    post {
        always {
            mail to: 'kravchenko.appleid@gmail.com',
                 subject: "Test Results for ${currentBuild.fullDisplayName}",
                 body: "Please see the test results at ${env.BUILD_URL}"
        }
    }
}
