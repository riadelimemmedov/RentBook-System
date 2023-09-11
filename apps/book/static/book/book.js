var book = new Vue({
    el: "#book",
    delimiters: ['[[', ']]'],
    data: {
        role:"alert",
        is_complete:false,
    },
    methods: {
        checkForm(e){
            const self = this
            const book_form = document.getElementById('book_form')

            const book_title = document.getElementById('id_book_title') 
            const book_publisher = document.getElementById('id_book_publisher')
            const book_author = document.getElementById('id_book_author')

            const csrf = document.getElementsByName('csrfmiddlewaretoken')



            console.log('Title: ',  book_title)
            console.log('Publisher Title: ',  book_publisher.options[book_publisher.selectedIndex].text)
            console.log('Author Title: ', book_author.options[book_author.selectedIndex].text)
            console.log('Csrf is ', csrf[0]);
            console.log('Book form ', book_form.action);

            const fd = new FormData()
            fd.append('csrfmiddlewaretoken', csrf[0].value)
            fd.append('book_title',book_title.value)
            fd.append('book_publisher',book_publisher.options[book_publisher.selectedIndex].text)
            fd.append('book_publisher',book_publisher.options[book_publisher.selectedIndex].value)

            fd.append('book_author',book_author.options[book_author.selectedIndex].text)
            fd.append('book_author',book_author.options[book_author.selectedIndex].value)


            
            $.ajax({
                type:'POST',
                url: book_form.action,
                enctype: 'multipart/form-data',
                data:fd,
                beforeSend : function(){
                    document.getElementById('alert_box').innerHTML = ''
                },
                success:function(response){
                    console.log('Succsess', response)
                    self.handleAlerts("bg-green-500 text-white font-bold rounded-t px-4 py-2","Succsess","border border-t-0 border-green-400 rounded-b bg-green-100 px-4 py-3 text-green-700","Book title created succsessfully.")
                },
                error:function(err){
                    self.handleAlerts("bg-red-500 text-white font-bold rounded-t px-4 py-2","Error","border border-t-0 border-red-400 rounded-b bg-red-100 px-4 py-3 text-red-700","Something went wrong please try again.")

                    console.log('Error ', err)
                },
                cache: false,
                contentType: false,
                processData: false,
            })
        },

        handleAlerts(notification_title_class,notification_title_text,notification_body_class,notification_body_text){
            const alert_box = document.getElementById('alert_box')
            alert_box.innerHTML = `
                <div role="alert">
                    <div class="${notification_title_class}">
                        ${notification_title_text}
                    </div>
                    <div class="${notification_body_class}">
                        <p>${notification_body_text}</p>
                    </div>
                </div>
            `
        }
    },
})
