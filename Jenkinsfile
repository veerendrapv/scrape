properties([
  parameters([
    string(name: 'module_name', defaultValue: 'ib_dev_efs'),
    string(name: 'email_recipients', defaultValue: 'veerendrapv@gmail.com'),
    // use the optional parameter 'rpm_branch_name' if you want to build RPMs
    // for a branch other than master branch.
    // string(name: 'rpm_branch_name', defaultValue: 'efs_migration'),
  ])
])

 stages {
    stage('Checkout') { // Checkout the repository containing your deploy automation
      steps {
        checkout scm
       }
     }
   }

post {
  success {
      msg = "Deploy succeeded for #{params.DEPLOY_APP} #{params.DEPLOY_VER} " +
              "to #{params.DEPLOY_ENV} #{ (${env.BUILD_URL})"
      slackSend message: msg, channel: env.SLACK_CHANNEL
  }
  failure {
    script {
      msg = "Deploy failed for #{params.DEPLOY_APP} #{params.DEPLOY_VER} " +
              "to #{params.DEPLOY_ENV} #{ (${env.BUILD_URL})"
      slackSend message: msg, channel: env.SLACK_CHANNEL
  }
}
}
