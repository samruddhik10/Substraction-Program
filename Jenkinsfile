pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v
                '''
            }
        }

        stage('Evidently Monitoring') {
            steps {
                sh '''
                . venv/bin/activate
                python monitoring.py
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'evidently_report.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline execution failed!'
        }
    }
}