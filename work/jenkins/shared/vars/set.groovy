def call(List extraParameters = [], forceAllParameters = false) {
    def defaultParameters = [
        booleanParam(
            description: 'opcja',
            name: 'OPCJA',
            defaultValue: false
        ),
    ]


    properties([
        parameters(defaultParameters + extraParameters)
    ])
}

