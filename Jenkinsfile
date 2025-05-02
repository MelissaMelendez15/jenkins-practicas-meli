


pipeline {
    
    agent any
    
    stages {
       
        stage ('Instalar dependencias') {

           when {
            not {
                branch 'develop'
            }
           }
           steps {
                sh 'pip3 install flask pytest requests --break-system-packages'
            }
        }

        stage('Echo') {
            when {
            not {
                branch 'develop'
            }
           }
            steps {
                echo 'Hola Meli, este es tu primer pipeline funcionando'
            }
        }

        stage('Clone') {
            when {
            not {
                branch 'develop'
            }
           }
            steps {
                git branch: 'main', url: 'https://github.com/MelissaMelendez15/jenkins-practicas-meli.git'
            }
        }

        stage ('Verificar archivos') {
          when {
            not {
                branch 'develop'
            }
           }
          steps {
            sh 'ls -la'
          }
        }

        stage ('Mostrar WORKSPACE') {
            when {
            not {
                branch 'develop'
            }
           }
            steps {
                sh 'echo $WORKSPACE'
            }
        }

         stage ('Build (simulado)') {
            when {
            not {
                branch 'develop'
            }
           }
            steps {
                echo 'Fase de Build simulada...'
            }
        }

        stage ('Iniciar Flask') {
            when {
            not {
                branch 'develop'
            }
           }
            steps {
                sh 'nohup python3 app/calc.py &'
                sh 'sleep 5'
            }
        }

        stage ('Iniciar Wiremock') {
            when {
            not {
                branch 'develop'
            }
           }
            steps {
                echo 'Iniciando Wiremock con ruta completa...'
                sh 'ls -la wiremock'
                sh 'nohup java -jar wiremock/wiremock-standalone-2.27.2.jar --port 8081 --root-dir wiremock &'
                sh 'sleep 10'
                echo 'Comprobando si Wiremock está vivo...'
                sh 'curl -v http://localhost:8081/__admin || echo "Wiremock no respondió"'
            }
        }
        
        stage ('Tests en paralelo') {
            when {
            not {
                branch 'develop'
            }
           }
            parallel {
               stage ('Unit') {
                 steps {
                  sh 'pytest test/unit --junitxml=results-unit.xml'
                }
            }

            stage ('Service') {
                  steps {
                   sh 'pytest test/rest --junitxml=results-service.xml'
                }
            }
            }
        }
    }

    post {
        always {
            junit 'results-*.xml'
        }
    }
}