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
    }
}