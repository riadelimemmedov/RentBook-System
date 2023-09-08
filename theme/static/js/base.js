var base = new Vue({
    el: "#base",
    delimiters: ['[[', ']]'],
    data: {
        counter: 0,
        is_dark_mode:null,
        reload_count:1
    },
    methods: {
        async changeMode(){            
            try{
                const response = await fetch('http://127.0.0.1:8000/change/',{
                    method:'POST',
                        headers:{
                            'Content-Type': 'application/json',
                        },
                        credentials: 'same-origin',
                    })
                    if (response.ok) {
                        const data = await response.json();
                        this.is_dark_mode = data.is_dark_mode;
                        const htmlElement = document.documentElement;
                        htmlElement.classList.contains('dark') ? htmlElement.classList.remove('dark') : htmlElement.classList.add('dark');
                    } else {
                        console.error('Failed to toggle dark mode');
                    }
            }
            catch(err){
                console.error('Error:', err);
            }
        }
    },
    mounted() {

      },
})
