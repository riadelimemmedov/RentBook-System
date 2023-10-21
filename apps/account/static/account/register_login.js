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
        validationResult:{}
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
            console.log('Least eigt number ', this.validationResult['least_eight_character'])
            console.log('Least uppercase ', this.validationResult['least_uppercase_character'])
            console.log('Least lowercase ', this.validationResult['least_lowercase_character'])
            console.log('Least number ', this.validationResult['least_one_number'])
            console.log('Least special ', this.validationResult['least_special_character'])
            console.log('Password is match ', this.validationResult['is_match'])
        }
    },

    computed:{
        // Check for at least 8 characters
        circleColorLeastEightCharacter(){
            let result = {'bg-green-500': this.password.length >= 8,'bg-red-500': this.password.length < 8};
            Object.values(result)[0] == true ? this.validationResult['least_eight_character'] = Object.values(result)[0] : delete this.validationResult.least_eight_character
            return result               
        },
        textColorLeastEightCharacter(){
            return {'text-green-500': this.password.length >= 8,'text-red-500': this.password.length < 8};
        },

        // Check for at least one uppercase letter
        circleColorLeastOneUpperCaseCharacter(){
            let result = {'bg-green-500': !!/[A-Z]/.test(this.password),'bg-red-500': !/[A-Z]/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_uppercase_character'] = Object.values(result)[0] : delete this.validationResult.least_uppercase_character
            return result
        },
        textColorLeastOneUpperCaseCharacter(){
            return {'text-green-500': !!/[A-Z]/.test(this.password),'text-red-500': !/[A-Z]/.test(this.password)}
        },  


        // Check for at least one lowercase letter
        circleColorLeastOneLowerCaseCharacter(){
            let result = {'bg-green-500': !!/[a-z]/.test(this.password),'bg-red-500': !/[A-Z]/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_lowercase_character'] = Object.values(result)[0] : delete this.validationResult.least_lowercase_character
            return result
        },
        textColorLeastOneLowerCaseCharacter(){
            return {'text-green-500': !!/[a-z]/.test(this.password),'text-red-500': !/[A-Z]/.test(this.password)}
        },


        // Check for at least one number
        circleColorLeastOneNumberCharacter(){
            let result = {'bg-green-500': !!/\d/.test(this.password),'bg-red-500': !!/\d/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_one_number'] = Object.values(result)[0] : delete this.validationResult.least_one_number
            return result
        },
        textColorLeastOneNumberCharacter(){
            return {'text-green-500': !!/\d/.test(this.password),'text-red-500': !!/\d/.test(this.password)}
        },


        // Check for at least one special character
        circleColorLeastOneSpecialCharacter(){
            let result = {'bg-green-500': !!/[!@#$%^&*]/.test(this.password),'bg-red-500': !/[!@#$%^&*]/.test(this.password)}
            Object.values(result)[0] == true ? this.validationResult['least_special_character'] = Object.values(result)[0] : delete this.validationResult.least_special_character
            return result
        },
        textColorLeastOneSpecialCharacter(){
            return {'text-green-500': !!/[!@#$%^&*]/.test(this.password),'text-red-500': !/[!@#$%^&*]/.test(this.password)}
        },


        //Check password is match or not
        circleColorMatchPassword(){
            let result = {'bg-green-500': this.password === this.repassword, 'bg-red-500': this.password !== this.repassword}
            Object.values(result)[0] == true ? this.validationResult['is_match'] = Object.values(result)[0] : delete this.validationResult.is_match
            return result
        },
        textColorMatchPassword(){
            return {'text-green-500': this.password === this.repassword, 'text-red-500': this.password !== this.repassword}
        }
    },

    mounted() {
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
