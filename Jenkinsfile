pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'paycare-etl'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url:'https://github.com/Fabthenabab/paycare.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'docker run --rm ${DOCKER_IMAGE} bash -c "pip install -r requirements.txt"'
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script{
                    sh """
                    docker run --rm \
                        -v "/tmp:/test_output" \
                        -e PYTHONPATH=/app \
                        ${DOCKER_IMAGE} \
                        bash -c "pytest --junitxml=/test_output/unit-tests.xml;ls -la /test_output;cp /test_output/unit-tests.xml /tmp//unit-tests.xml"
                    """
                    sh 'ls -la /tmp'
                } 
            }
            post {
                always {
                    junit '/tmp/unit-tests.xml'  // Publish test results
                }
            }
        }
        

        stage('Run Docker Container') {
            steps {
                script {
                    // Create input data file dynamically
                    sh 'echo "employee_id,employee_name,salary\n101,Alice,5000\n102,Bob,7000" > input_data.csv'

                    // Run the Docker container with mounted input/output files
                    sh 'docker run --rm -v $(pwd)/input_data.csv:/app/input_data.csv -v $(pwd)/output_data.csv:/app/output_data.csv ${DOCKER_IMAGE}'
                }
            }
        }
    }

    post {
        success {
            echo 'ETL Pipeline completed successfully!'
            // Optionally send notification (Slack/Email)
        }
        failure {
            echo 'ETL Pipeline failed.'
            // Optionally send notification (Slack/Email)
        }
    }
}
