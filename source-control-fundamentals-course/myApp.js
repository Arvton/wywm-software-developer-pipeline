//testing out adding a file to local repo. then staging the file with git add, and git commit to commit to local repo, and git push -u origin main

//testing the addition of new code in a new branch
const myApp = {
    name:"Demo App for Git",
    version: "1.0.0",
    Author: "WYWM - Arvin Josol",
    description: "This is a simple app",
    license: "MIT",
    year: "2022",
    website: "https://myapp.com",

    sayHello: function () {
        console.log(`Hello from ${this.name} v${this.version}`);
    },

    sayGoodbye: function () {
        console.log(`Goodbye from ${this.name} v${this.version}`);
    },

    saySomething: function (somthing) {
        console.log(`${this.name} says: v${something}`);
    },

    init: function () {
        console.log(`${this.name} ${this.version}`);
    },
}

myApp.init();