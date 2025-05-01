pipeline {
    
    agent any

    stages {

        stage ('Instalar dependencias') {
            steps {
                sh 'pip3 install flask pytest requests --break-system-packages'
            }
        }

        stage('Echo') {
            steps {
                echo 'Hola Meli, este es tu primer pipeline funcionando'
            }
        }

        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/MelissaMelendez15/jenkins-practicas-meli.git'
            }
        }

        stage ('Verificar archivos') {
          steps {
            sh 'ls -la'
          }
        }

        stage ('Mostrar WORKSPACE') {
            steps {
                sh 'echo $WORKSPACE'
            }
        }

         stage ('Build (simulado)') {
            steps {
                echo 'Fase de Build simulada...'
            }
        }

        stage ('Unit') {
            steps {
                sh 'pytest test/unit'
            }
        }

        stage ('Iniciar Flask') {
            steps {
                sh 'nohup python3 app/calc.py &'
                sh 'sleep 5'
            }
        }

        stage ('Iniciar Wiremock') {
            steps {
                sh 'java -jar wiremock-standalone-2.27.2.jar --port 8081 --root-dir wiremock &'
                sh 'sleep 5'
            }
        }
        
        stage ('Service') {
            steps {
                sh 'pytest test/rest'
            }
        }
    }
}