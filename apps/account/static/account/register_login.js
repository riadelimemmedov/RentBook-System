var register_login = new Vue({
    el: "#register_login",
    delimiters: ['[[', ']]'],
    data: {
        phone:null,
        password:null,
        showPassword: false,
        repassword:null,
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
        },
        checkPassword(){
        },


        passwordLengthClass(feature,classType,element_id){
            // return { 'bg-green-500': this.password.length >= 8, 'bg-red-500': this.password.length < 8 };
            return this.generateClass(feature,classType,this.password.length >= 8,element_id);
        },
        passwordLengthTextClass(feature,classType,element_id){
            // return { 'text-green-500': this.password.length >= 8, 'text-red-500': this.password.length < 8 };
            return this.generateClass(feature,classType,this.password.length >= 8,element_id);
        },

        passwordUppercaseClass(){
            return { 'bg-green-500': !!/[A-Z]/.test(this.password), 'bg-red-500': !/[A-Z]/.test(this.password) };
        },
        passwordUppercaseTextClass(){
            return { 'text-green-500': !!/[A-Z]/.test(this.password), 'text-red-500': !/[A-Z]/.test(this.password) };
        },

        generateClass(feature,classType,condition,element_id) {
            console.log('Element id is ', element_id)
            const bgClass = condition ? 'bg-green-500' : 'bg-red-500';
            const textClass = condition ? 'text-green-500' : 'text-red-500';

            const abs = this.$refs.bgId
            console.log('Some ', abs)

            return {
                [bgClass]: true,
                [textClass]: condition && textClass !== undefined,
            };

        },
        
    },
    mounted() {
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
