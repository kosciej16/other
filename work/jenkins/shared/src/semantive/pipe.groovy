class Pipe {
    Script scr
    String path

    Pipe(Script scr) {
        this.scr = scr
    }

    def prepare_container() {
        this.path = this.scr.sh(script:'mktemp --directory', returnStdout: true)
        scr.stage("prepare container") {
            new prepareDefaultContainer().call(venvPath: path)
        }
    }
}
