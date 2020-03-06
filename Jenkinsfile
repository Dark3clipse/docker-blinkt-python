pipeline {
  agent any
  options {
	skipStagesAfterUnstable()
  }
  stages {
    stage('test environment') {
      steps {
		sh 'docker --version && docker-compose --version'
      }
    }
    stage('build') {
      steps {
        sh 'make'
      }
    }

    stage('deploy') {
      steps {
        sh 'docker-compose -p blinkt up -d'
      }
    }
  }
  post {
  	  always {
  	    echo 'build finished'
  	  }
  	  success {
  		echo 'was stable'
  	  }
  	  unstable {
  	    echo 'had failures'
  	  }
  	}
}
