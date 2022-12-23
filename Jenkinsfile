node {
    def app
    environment {
        registry = "jumper93/zin4y_node"   
        registryCredential = 'c6f696d0-3272-44b1-a4ce-52d7860e3b5e'

    }

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build('zinchenko-ihor/test')
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. 
         *docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'*/
         * sh 'sudo -S docker login -u "jumper93" -p "" '
           docker.withRegistry( '', registryCredential ) {    
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    }
}
