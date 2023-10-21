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
        upperCaseText:'upperCaseText',
        validationResult:{},
        isAgree:false,
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

        getResult(e){
            e.preventDefault();
        },

        registerForm(e){
            e.preventDefault()
            console.log('Register form triggered')
        }
    },

    computed:{
        // Check for at least 8 characters
        circleColorLeastEightCharacter(){
            let result = {'bg-success': this.password.length >= 8,'bg-danger': this.password.length < 8};
            Object.values(result)[0] == true ? this.validationResult['least_eight_character'] = Object.values(result)[0] : delete this.validationResult.least_eight_character
            return result               
        },
        textColorLeastEightCharacter(){
            return {'text-success': this.password.length >= 8,'text-danger': this.password.length < 8};
        },

        // Check for at least one uppercase letter
        circleColorLeastOneUpperCaseCharacter(){
            let result = {'bg-success': !!/[A-Z]/.test(this.password),'bg-danger': !/[A-Z]/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_uppercase_character'] = Object.values(result)[0] : delete this.validationResult.least_uppercase_character
            return result
        },
        textColorLeastOneUpperCaseCharacter(){
            return {'text-success': !!/[A-Z]/.test(this.password),'text-danger': !/[A-Z]/.test(this.password)}
        },  


        // Check for at least one lowercase letter
        circleColorLeastOneLowerCaseCharacter(){
            let result = {'bg-success': !!/[a-z]/.test(this.password),'bg-danger': !/[a-z]/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_lowercase_character'] = Object.values(result)[0] : delete this.validationResult.least_lowercase_character
            return result
        },
        textColorLeastOneLowerCaseCharacter(){
            return {'text-success': !!/[a-z]/.test(this.password),'text-danger': !/[a-z]/.test(this.password)}
        },


        // Check for at least one number
        circleColorLeastOneNumberCharacter(){
            let result = {'bg-success': !!/\d/.test(this.password),'bg-danger': !/\d/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_one_number'] = Object.values(result)[0] : delete this.validationResult.least_one_number
            return result
        },
        textColorLeastOneNumberCharacter(){
            return {'text-success': !!/\d/.test(this.password),'text-danger': !/\d/.test(this.password)}
        },


        // Check for at least one special character
        circleColorLeastOneSpecialCharacter(){
            let result = {'bg-success': !!/[!@#$%^&*]/.test(this.password),'bg-danger': !/[!@#$%^&*]/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_special_character'] = Object.values(result)[0] : delete this.validationResult.least_special_character
            return result
        },
        textColorLeastOneSpecialCharacter(){
            return {'text-success': !!/[!@#$%^&*]/.test(this.password),'text-danger': !/[!@#$%^&*]/.test(this.password)}
        },


        //Check password is match or not
        circleColorMatchPassword(){
            let result = {'bg-success': this.password === this.repassword, 'bg-danger': this.password !== this.repassword}
            Object.values(result)[0] == true ? this.validationResult['is_match'] = Object.values(result)[0] : delete this.validationResult.is_match
            return result
        },
        textColorMatchPassword(){
            return {'text-success': this.password === this.repassword, 'text-danger': this.password !== this.repassword}
        }
    },

    mounted() {
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
