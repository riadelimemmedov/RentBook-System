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
        selected_letter:null,
        book_titles:null,
        book_titles_object:null,
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
            console.log('blett ', book_title,book_publisher,book_author);
            const fd = new FormData()
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            console.log(csrf[0].value);
            fd.append('book_title',book_title.value)
            console.log(book_title.value);
            fd.append('book_publisher',book_publisher.options[book_publisher.selectedIndex].text)
            console.log(book_publisher.options[book_publisher.selectedIndex].text);
            console.log(book_publisher.options[book_publisher.selectedIndex]);
            fd.append('book_publisher',book_publisher.options[book_publisher.selectedIndex].value)
            console.log(book_publisher.options[book_publisher.selectedIndex].value);
            fd.append('book_author',book_author.options[book_author.selectedIndex].text)
            console.log(book_author.options[book_author.selectedIndex].text);
            fd.append('book_author',book_author.options[book_author.selectedIndex].value)
            console.log(book_author.options[book_author.selectedIndex].value);
            console.log('Bunedi laa ', fd)
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

        handleSwalNotifications(title,icon,confirmButtonText){
            Swal.fire({
                title: title,
                icon: icon,
                confirmButtonText: confirmButtonText
            })
        },


        getFieldsError(fields,is_error){
            let arr = fields
            let error_field_arr = []
            for (let i = 0; i < fields.length; i++) {
                // Parse the current element into a JavaScript object
                let obj = JSON.parse(arr[i].replace(/'/g, "\""));//This raemain this format,because if we have call continuesly call parse function javascript heap return error.Maximum call stack
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


        searchBookTitle(letter){
            const self = this
            self.selected_letter = letter
            $.ajax({
                type:'GET',
                url: `http://127.0.0.1:8000/book/${letter}/`,
                success:function(response){
                    let obj = self.parseObject(response.book_titles)
                    self.book_titles_object = obj
                    obj.length < 3 ? self.book_titles=obj : self.book_titles=obj.slice(obj.length - 3,obj.length)
                    self.book_titles.length > 0 ? null : self.handleSwalNotifications('Not found any book title','info','Close')
                },
                error:function(err){
                    self.handleSwalNotifications('Please try again','error','Close')
                }
            })
        },


        parseObject(obj){
            let parsed_obj = JSON.parse(obj.replace(/'/g, "\""));
            return parsed_obj
        },

        openForm(){
            this.$refs.formModal.classList.remove('hidden')
        },


        cancelForm(e){
            this.$refs.formModal.classList.add('hidden')
        },


        getFormModal(e){
            e.target.id  == 'backdrop' ? this.$refs.formModal.classList.add('hidden') : null
        },


        getAllSearchResult(e){
            e.preventDefault();
            let url = this.modifyLink(e.target.href)
            window.location.href = url
        },


        modifyLink(url){
            let modifiedUrl = `${url.split('/').slice(0, -2).join('/')}/${this.selected_letter}`;
            return modifiedUrl
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

