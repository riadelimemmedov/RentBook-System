var register_login = new Vue({
    el: "#register_login",
    delimiters: ['[[', ']]'],
    data: {
        phone:null,
        password:null,
        showPassword: false,
        repassword:null,
        showRepassword:false,
        type:null,
        uppercaseBg:'uppercaseBg',
        upperCaseText:'upperCaseText'
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
        },
        
        checkPassword(){
        },

        passwordUppercaseClass(){
            return {
                'bg-green-500': this.password.length > 8,
                'bg-red-500': this.password.length < 8,
            };
        },
        passwordUppercaseTextClass(){
            return {
                'text-green-500': this.password.length > 8,
                'text-red-500': this.password.length < 8,
            };
        },        
    },
    mounted() {
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
