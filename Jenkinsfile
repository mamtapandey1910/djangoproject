pipeline {
  agent any {
    stages {
      stage (build){
        steps {
          sh 'docker build -t jenkinsdocker .'
        }
      }
      stage (image security scan){
        steps {
           sh 'echo "Hello image"'
        }
      }
      stage (deploy){
        steps {
           sh 'echo "Hello deploy"'
        }
      }
      stage (validate){
        steps {
          sh 'echo "Hello validate"'
        }
      }
      stage (post){
        steps {
           sh 'echo "Hello post"'
        }
      }
    }
  }
}
