var register_login = new Vue({
    el: "#register_login",
    delimiters: ['[[', ']]'],
    data: {
        //Form input value
        first_name:null,
        last_name:null,
        gender:null,
        account_type:null,
        email:null,
        phone:null,
        password:null,
        repassword:null,

        //Other value
        showPassword: false,
        showRepassword:false,
        type:null,
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


        setErrorClass(field,class_name){
            if(Array.isArray(field)){
                field.forEach(ref=>ref.classList.add(class_name))
            }
            else{
                if(field.classList.contains('border-danger')){
                    field.classList.remove('border-danger')
                }
                else{
                    field.classList.add('border-danger')
                }
            }
        },

        isValidEmail(){
            !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email) ? this.$refs.email.classList.add('border-danger') :  this.$refs.email.classList.remove('border-danger')
        },

        isValidPhoneNumber(){
            !/^\d+$/.test(this.phone) ? this.$refs.phone.classList.add('border-danger') : this.$refs.phone.classList.remove('border-danger') 
        },

        validateFormField(){
            this.isValidEmail()
            this.isValidPhoneNumber()

            let form_field_value = {
                "first_name":this.first_name,
                "last_name":this.last_name,
                // "email":this.email,
                // "phone":this.phone,
                // "password":this.password,
                // "repassword":this.repassword,
            }

            for (let key in form_field_value) {
                form_field_value[key] == null || form_field_value[key] == '' ? this.$refs[key].classList.add('border-danger') : this.$refs[key].classList.remove('border-danger')
            }
            Object.keys(this.validationResult).length!=6 ? [this.$refs.password, this.$refs.repassword].forEach(ref => ref.classList.add('border-danger')) : [this.$refs.password, this.$refs.repassword].forEach(ref => ref.classList.remove('border-danger'));
        },

        registerForm(e){
            e.preventDefault()
            const isValidForm = this.validateFormField()
            console.log('Is valid form ', isValidForm) 
        },

        handleGender(type) {
            if(type=='Female'){
                this.$refs.male.classList.remove('shadow-lg','bg-body');
                this.$refs.female.classList.add('shadow-lg','bg-body');
            }
            else if(type=='Male'){
                this.$refs.female.classList.remove('shadow-lg','bg-body');
                this.$refs.male.classList.add('shadow-lg','bg-body');
            }
            this.gender = type;
        },

        handleAccountType(type){
            if(type=='Buyer'){
                this.$refs.seller.classList.remove('shadow-lg','bg-body');
                this.$refs.buyer.classList.add('shadow-lg','bg-body');
            }
            else if(type=='Seller'){
                this.$refs.buyer.classList.remove('shadow-lg','bg-body');
                this.$refs.seller.classList.add('shadow-lg','bg-body');
            }
            this.account_type = type
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
        },
    },

    mounted() {
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {utilsScript:"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",});
    },
})
