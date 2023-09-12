var book = new Vue({
    el: "#book",
    delimiters: ['[[', ']]'],
    data: {
        role:"alert",
        is_complete:false,
        show:true,
        is_submit:true,
        errors:null,
        errors_field:null,
    },
    methods: {
        checkForm(e){
            const self = this
            const book_form = document.getElementById('book_form')
            const book_title = document.getElementById('id_book_title') 
            const book_publisher = document.getElementById('id_book_publisher')
            const book_author = document.getElementById('id_book_author')
            const csrf = document.getElementsByName('csrfmiddlewaretoken')

            const fd = self.getBookTitleForm(csrf, book_title, book_publisher, book_author)
            // const checkedForm = self.checkFormFields([csrf[0].value, book_title.value, book_publisher.options[book_publisher.selectedIndex].text, book_author.options[book_author.selectedIndex].text])
            // const create_book_btn = self.$refs.create_book_btn
            // console.log('Create book btn is ', create_book_btn);


            if(fd){
                $.ajax({
                    type:'POST',
                    url: book_form.action,
                    enctype: 'multipart/form-data',
                    data:fd,
                    beforeSend : function(){
                        self.$refs.alert_box.innerHTML = ''
                        self.errors = null
                        // self.$refs.alert_field_box.innerHTML = ''
                    },
                    success:function(response){
                        let fields_error = self.getFieldsError(self.errors_field,false)
                        self.handleAlerts("Book title created succsessfully",'success')//This is notification,Show user book creating process complete or not.Now show field erros or etc
                    },
                    error: function(err){
                        self.errors_field = err.responseJSON.form_errors
                        let fields_error = self.getFieldsError(self.errors_field,true)
                        self.errors = fields_error ? fields_error : self.handleAlerts("Something went wrong please try again",'danger') //This is notification,Show user book creating process complete or not.Now show field erros or etc
                        
                        // self.hideAlertCarts
                    },
                    cache: false,
                    contentType: false,
                    processData: false,
                })
            }
        },

        getBookTitleForm(csrf,book_title,book_publisher,book_author){
            const fd = new FormData()
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('book_title',book_title.value)
            fd.append('book_publisher',book_publisher.options[book_publisher.selectedIndex].text)
            fd.append('book_publisher',book_publisher.options[book_publisher.selectedIndex].value)
            fd.append('book_author',book_author.options[book_author.selectedIndex].text)
            fd.append('book_author',book_author.options[book_author.selectedIndex].value)
            return fd
        },

        
        handleAlerts(text,type){
            this.$refs.alert_box.innerHTML =  `
                        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                            <strong>${text}</strong> 
                            <button type="button" class="btn-close fw-bold" data-bs-dismiss="alert" aria-label="Close"></button>
                        </div>
                `
        },


        getFieldsError(fields,is_error){
            let arr = fields
            let error_field_arr = []
            for (let i = 0; i < fields.length; i++) {
                // Parse the current element into a JavaScript object
                let obj = JSON.parse(arr[i].replace(/'/g, "\""));
                error_field_arr.push(Object.values(obj))
                if(is_error){
                    document.getElementsByName(Object.keys(obj)[0])[0].classList.add('form-control')
                    document.getElementsByName(Object.keys(obj)[0])[0].classList.add('is-invalid')
                }
                else{
                    document.getElementsByName(Object.keys(obj)[0])[0].classList.remove('form-control')
                    document.getElementsByName(Object.keys(obj)[0])[0].classList.remove('is-invalid')
                }
            }
            return error_field_arr
        },

        extractText(error) {
            return error[0]
        },

        // hideAlertCart(){
        //         setTimeout(()=>{
        //             this.$refs.alert_box.innerHTML = ''
        //         },5000)
        // },

        // checkFormFields(form_fields_value){
        //     let count = 0
        //     form_fields_value.forEach(element => {
        //         element != '' ? count++ : null 
        //     });
        //     this.is_submit=false ? count==form_fields_value.length : null
        // }
    },
})

