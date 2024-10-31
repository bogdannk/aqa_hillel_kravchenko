pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11.9'
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/bogdannk/aqa_hillel_kravchenko.git', branch: 'homework_31'
            }
        }

        stage('Install Python with pyenv') {
            steps {
                script {
                    sh '''
                        # Установка pyenv и Python
                        if ! command -v pyenv &> /dev/null; then
                            echo "pyenv не найден. Устанавливаем..."
                            curl https://pyenv.run | bash
                        else
                            echo "pyenv уже установлен."
                        fi

                        # Настройка pyenv
                        export PATH="$HOME/.pyenv/bin:$PATH"
                        eval "$(pyenv init --path)"
                        eval "$(pyenv init -)"

                        # Установка нужной версии Python
                        if ! pyenv versions | grep -q ${PYTHON_VERSION}; then
                            pyenv install ${PYTHON_VERSION}
                        fi
                        pyenv global ${PYTHON_VERSION}
                    '''
                }
            }
        }

        stage('Create Python Virtual Environment') {
            steps {
                script {
                    sh '''
                        # Создание виртуального окружения
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
                    sh '''
                        # Активация виртуального окружения и установка зависимостей
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
                    sh '''
                        # Запуск тестов
                        source ${VENV_DIR}/bin/activate
                        pytest --maxfail=1 --disable-warnings -q --junitxml=test-results.xml tests/
                    '''
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                junit 'test-results.xml'  // Указываем путь к файлу результатов тестов
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
