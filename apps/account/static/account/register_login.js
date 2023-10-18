var register_login = new Vue({
    el: "#register_login",
    delimiters: ['[[', ']]'],
    data: {
        phone:null,
        showPassword: false,
        showRepassword:false,
        type:null
    },
    methods: {
        toggleShowPassword(type=null){
            type=='password' ? this.togglePassword() : this.toggleRepassword()
        },
        togglePassword(){
            this.showPassword = !this.showPassword;
        },
        toggleRepassword(){
            this.showRepassword = !this.showRepassword;
        }
    },
    mounted() {
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
