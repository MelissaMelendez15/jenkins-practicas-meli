pipeline {
    
    agent any

    stages {
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

        stage ('Service') {
            steps {
                sh 'pytest test/rest'
            }
        }
    }
}