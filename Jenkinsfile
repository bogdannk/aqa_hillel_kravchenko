pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo "Checking out code from Git..."
                    git url: 'https://github.com/bogdannk/aqa_hillel_kravchenko.git', branch: 'homework_31'
                }
            }
        }

        stage('Install Python with pyenv') {
            steps {
                script {
                    echo "Installing Python version ${PYTHON_VERSION} with pyenv..."
                    sh '''
                        # Проверка, установлен ли pyenv
                        if ! command -v pyenv &> /dev/null; then
                            echo "pyenv не найден. Устанавливаем..."
                            curl https://pyenv.run | bash
                        else
                            echo "pyenv уже установлен."
                        fi

                        # Добавление pyenv в PATH
                        export PATH="$HOME/.pyenv/bin:$PATH"
                        eval "$(pyenv init --path)"
                        eval "$(pyenv init -)"

                        # Установка и активация нужной версии Python
                        echo "Проверяем, установлена ли версия Python ${PYTHON_VERSION}..."
                        if ! pyenv versions | grep -q ${PYTHON_VERSION}; then
                            echo "Устанавливаем Python ${PYTHON_VERSION}..."
                            pyenv install ${PYTHON_VERSION}
                        else
                            echo "Python ${PYTHON_VERSION} уже установлен."
                        fi
                        echo "Активация версии Python ${PYTHON_VERSION}..."
                        pyenv global ${PYTHON_VERSION}
                    '''
                }
            }
        }

        stage('Create Python Virtual Environment') {
            steps {
                script {
                    echo "Creating Python virtual environment..."
                    sh '''
                        if [ ! -d "${VENV_DIR}" ]; then
                            echo "Создаём виртуальное окружение..."
                            python -m venv ${VENV_DIR}
                        else
                            echo "Виртуальное окружение уже существует."
                        fi
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    echo "Installing dependencies from requirements.txt..."
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    echo "Running tests with pytest..."
                    sh '''
                        source ${VENV_DIR}/bin/activate
                        pytest --maxfail=1 --disable-warnings -q tests/
                    '''
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                script {
                    echo "Publishing test results..."
                    junit '**/test-*.xml'  // Предполагается, что результаты тестов в формате JUnit XML
                }
            }
        }
    }

    post {
        always {
            script {
                echo "Checking build result..."
                // Проверка, установлен ли почтовый сервер
                if (currentBuild.result == 'FAILURE') {
                    echo 'Ошибка при выполнении сборки. Проверка почтовых уведомлений отключена.'
                } else {
                    echo "Sending email with test results to kravchenko.appleid@gmail.com..."
                    mail to: 'kravchenko.appleid@gmail.com',
                         subject: "Test Results for ${currentBuild.fullDisplayName}",
                         body: "Please see the test results at ${env.BUILD_URL}"
                }
            }
        }
    }
}
