def call(Script scr, String name) {
    scr.stage(name) {
        scr.echo "Triggering ${name} stage..."
        // scr.echo "${MOJSTRING}"
    }
}
