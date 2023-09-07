var base = new Vue({
    el: "#base",
    delimiters: ['[[', ']]'],
    data: {
        counter: 0,
        input_text:null,
    },
    methods: {
        changeMode(){
            console.log('Noldu ala')
            fetch('http://127.0.0.1:8000/change')
                .then((response) => {
                    console.log('Work and change ', response)
                })
                .catch((err) => {
                    console.log('Error ', err)
                })
        }
    }
})
