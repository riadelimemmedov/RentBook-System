var register_login = new Vue({
    el: "#register_login",
    delimiters: ['[[', ']]'],
    data: {
        phone:null
    },
    methods: {
    },
    mounted() {
        const sidebar = document.getElementById('sidebar').classList.replace('h-screen','h-full')
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
