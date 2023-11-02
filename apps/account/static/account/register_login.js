var register_login = new Vue({
    el: "#register_login",
    delimiters: ['[[', ']]'],
    data: {
        //Form input value
        first_name: null,
        last_name: null,
        gender: null,
        account_type: null,
        email: null,
        phone: null,
        password: null,
        repassword: null,

        //Other value
        showPassword: false,
        showRepassword: false,
        type: null,
        validationResult: {},
        isAgree: false,
        isRregisterLogin: null,

        is_valid_login_form: false,
        isValidRegisterForm: false
    },
    methods: {
        toggleShowPassword(type = null) {
            type == 'password' ? this.togglePassword() : this.toggleRepassword()
        },
        togglePassword() {
            this.showPassword = !this.showPassword;
        },
        toggleRepassword() {
            this.showRepassword = !this.showRepassword;
        },

        checkPassword() {},

        getResult(e) {
            e.preventDefault();
        },

        resetForm() {
            Object.assign(this, {
                email: '',
                password: ''
            });
        },

        checkIsNull(input_field_value, input_field_type) {
            // this.$refs.login_password.classList.add('border-danger') ? input_field_value == '' && input_field_type == 'password' : this.$refs.login_email.classList.add('border-danger')
            return input_field_value !== '';
        },

        toggleLoginRegister(type) {
            this.resetForm()
            this.isRregisterLogin = true ? type == 'login' : this.isRregisterLogin = false
        },

        checkRegisterLoginType() {
            const searched_path = "login"; //Default
            const current_path = `${window.location.pathname}`;
            const regex = new RegExp(searched_path);
            this.isRregisterLogin = true ? regex.test(current_path) : this.isRregisterLogin = false
        },


        setErrorClass(field, class_name) {
            if (Array.isArray(field)) {
                field.forEach(ref => ref.classList.add(class_name))
            } else {
                if (field.classList.contains('border-danger')) {
                    field.classList.remove('border-danger')
                } else {
                    field.classList.add('border-danger')
                }
            }
        },

        isValidEmail(event_name = null) {
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.email)) {
                event_name === 'login' ? this.$refs.login_email.classList.add('border-danger') : event_name === 'register' ? this.$refs.register_email.classList.add('border-danger') : null;
                return false;
            } else {
                event_name === 'login' ? this.$refs.login_email.classList.remove('border-danger') : event_name === 'register' ? this.$refs.register_email.classList.remove('border-danger') : null
                return true;
            }

        },

        isValidPhoneNumber() {
            if (!/^\d+$/.test(this.phone)) {
                this.$refs.phone.classList.add('border-danger')
                return false;
            } else {
                this.$refs.phone.classList.remove('border-danger')
                return true;
            }
        },

        isValidFirstLastName(formField) {
            let fieldNumber = 0
            for (let key in formField) {
                if (formField[key] == null || formField[key] == '') {
                    fieldNumber++
                    this.$refs[key].classList.add('border-danger')
                } else {
                    this.$refs[key].classList.remove('border-danger')
                }
            }
            if (fieldNumber <= 2 && fieldNumber > 0) {
                return false
            } else {
                return true
            }
        },

        validatePasswordField() {
            if (Object.keys(this.validationResult).length != 6) {
                [this.$refs.register_password, this.$refs.repassword].forEach(ref => ref.classList.add('border-danger'))
                return false
            } else {
                [this.$refs.register_password, this.$refs.repassword].forEach(ref => ref.classList.remove('border-danger'))
                return true
            }
        },

        validateUserMembershipAgreement() {
            if (!this.isAgree) {
                this.$refs.isAgree.classList.add('border-danger')
                return false
            } else {
                this.$refs.isAgree.classList.remove('border-danger')
                return true
            }
        },

        validateRegisterForm(event_name = null) {
            const isValidEmail = this.isValidEmail(event_name)
            const isValidPhoneNumber = this.isValidPhoneNumber()
            const isValidFirstLastName = this.isValidFirstLastName({
                "first_name": this.first_name,
                "last_name": this.last_name
            })
            const isValidPassword = this.validatePasswordField()
            const isValidMembershipAggrement = this.validateUserMembershipAgreement()

            return isValidEmail && isValidPhoneNumber && isValidFirstLastName && isValidPassword && isValidMembershipAggrement;
        },

        registerForm(e) {
            const isValidRegisterForm = this.validateRegisterForm(e.target.getAttribute('data_form_name'))
            console.log('Is valid form ', isValidRegisterForm)
        },

        handleGender(type) {
            if (type == 'Female') {
                this.$refs.male.classList.remove('shadow-lg', 'bg-body');
                this.$refs.female.classList.add('shadow-lg', 'bg-body');
            } else if (type == 'Male') {
                this.$refs.female.classList.remove('shadow-lg', 'bg-body');
                this.$refs.male.classList.add('shadow-lg', 'bg-body');
            }
            this.gender = type;
        },

        handleAccountType(type) {
            if (type == 'Buyer') {
                this.$refs.seller.classList.remove('shadow-lg', 'bg-body');
                this.$refs.buyer.classList.add('shadow-lg', 'bg-body');
            } else if (type == 'Seller') {
                this.$refs.buyer.classList.remove('shadow-lg', 'bg-body');
                this.$refs.seller.classList.add('shadow-lg', 'bg-body');
            }
            this.account_type = type
        },


        // validateLoginForm(event) {
        //     console.log('Password os ', this.password)
        //     this.password == null || this.password == '' ? this.$refs.login_password.classList.add('border-danger') : (this.password != null || this.password != '' ? this.$refs.login_password.classList.remove('border-danger') : null)
        //     this.email == null || this.email == '' ? this.$refs.login_email.classList.add('border-danger') : (this.email != null || this.email != '' ? this.isValidEmail(event.target.getAttribute('data_form_name')) : null)

        //     return (
        //         (this.$refs.login_password.classList.contains('border-danger') && (this.password === '' || this.password == null)) &&
        //         (this.$refs.login_email.classList.contains('border-danger') && (this.email === '' || this.email == null ? this.isValidEmail(event.target.getAttribute('data_form_name')):false))
        //     );
        // },

        validateLoginForm(event) {
            let isPasswordValid = !(this.password == null || this.password == '');
            let isEmailValid = !(this.email == null || this.email == '');

            this.$refs.login_password.classList.toggle('border-danger', !isPasswordValid);
            this.$refs.login_email.classList.toggle('border-danger', !isEmailValid);

            if (isEmailValid) {
                isEmailValid = this.isValidEmail(event.target.getAttribute('data_form_name'));
            }
            return isPasswordValid && isEmailValid;
        },


        loginForm(e) {
            const isValidLoginForm = this.validateLoginForm(e)
            if (isValidLoginForm) {
                this.is_valid_login_form = true
            } else {
                this.is_valid_login_form = false
                e.preventDefault()
            }
        }
    },

    computed: {
        // Check for at least 8 characters
        circleColorLeastEightCharacter() {
            let result = {
                'bg-success': this.password.length >= 8,
                'bg-danger': this.password.length < 8
            };
            Object.values(result)[0] == true ? this.validationResult['least_eight_character'] = Object.values(result)[0] : delete this.validationResult.least_eight_character
            return result
        },
        textColorLeastEightCharacter() {
            return {
                'text-success': this.password.length >= 8,
                'text-danger': this.password.length < 8
            };
        },

        // Check for at least one uppercase letter
        circleColorLeastOneUpperCaseCharacter() {
            let result = {
                'bg-success': !!/[A-Z]/.test(this.password),
                'bg-danger': !/[A-Z]/.test(this.password)
            }
            Object.values(result)[0] == true ? this.validationResult['least_uppercase_character'] = Object.values(result)[0] : delete this.validationResult.least_uppercase_character
            return result
        },
        textColorLeastOneUpperCaseCharacter() {
            return {
                'text-success': !!/[A-Z]/.test(this.password),
                'text-danger': !/[A-Z]/.test(this.password)
            }
        },


        // Check for at least one lowercase letter
        circleColorLeastOneLowerCaseCharacter() {
            let result = {
                'bg-success': !!/[a-z]/.test(this.password),
                'bg-danger': !/[a-z]/.test(this.password)
            }
            Object.values(result)[0] == true ? this.validationResult['least_lowercase_character'] = Object.values(result)[0] : delete this.validationResult.least_lowercase_character
            return result
        },
        textColorLeastOneLowerCaseCharacter() {
            return {
                'text-success': !!/[a-z]/.test(this.password),
                'text-danger': !/[a-z]/.test(this.password)
            }
        },


        // Check for at least one number
        circleColorLeastOneNumberCharacter() {
            let result = {
                'bg-success': !!/\d/.test(this.password),
                'bg-danger': !/\d/.test(this.password)
            }
            Object.values(result)[0] == true ? this.validationResult['least_one_number'] = Object.values(result)[0] : delete this.validationResult.least_one_number
            return result
        },
        textColorLeastOneNumberCharacter() {
            return {
                'text-success': !!/\d/.test(this.password),
                'text-danger': !/\d/.test(this.password)
            }
        },


        // Check for at least one special character
        circleColorLeastOneSpecialCharacter() {
            let result = {
                'bg-success': !!/[!@#$%^&*]/.test(this.password),
                'bg-danger': !/[!@#$%^&*]/.test(this.password)
            }
            Object.values(result)[0] == true ? this.validationResult['least_special_character'] = Object.values(result)[0] : delete this.validationResult.least_special_character
            return result
        },
        textColorLeastOneSpecialCharacter() {
            return {
                'text-success': !!/[!@#$%^&*]/.test(this.password),
                'text-danger': !/[!@#$%^&*]/.test(this.password)
            }
        },


        //Check password is match or not
        circleColorMatchPassword() {
            let result = {
                'bg-success': this.password === this.repassword,
                'bg-danger': this.password !== this.repassword
            }
            Object.values(result)[0] == true ? this.validationResult['is_match'] = Object.values(result)[0] : delete this.validationResult.is_match
            return result
        },
        textColorMatchPassword() {
            return {
                'text-success': this.password === this.repassword,
                'text-danger': this.password !== this.repassword
            }
        },
    },

    mounted() {
        this.checkRegisterLoginType()
        const phoneInputField = this.$refs.phone
        const phoneInput = window.intlTelInput(phoneInputField, {
            utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
        });
    },
})