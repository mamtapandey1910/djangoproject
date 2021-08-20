pipeline {
  agent any {
    stages {
      stage (build){
        steps {
          sh 'docker build -t --name dockerimage -p 8000:8000 jenkinsdocker .'
        }
      }
      stage (image security scan){
        steps {
          abc....
        }
      }
      stage (deploy){
        steps {
          abc.......
        }
      }
      stage (validate){
        steps {
          abc.......
        }
      }
      stage (post){
        steps {
          abc.....
        }
      }
    }
  }
}
