var search = new Vue({
    el: "#search",
    delimiters: ['[[', ']]'],
    data:{
        paged_books: null,
        has_previous: false,
        has_next: null,
        previous_page_number:null,
        next_page_number:null
    },
    methods: {
        loadPage(e) {
            // e.preventDefault()
            // $.ajax({
            //     type: 'GET',
            //     url: e.target.href,
            //     success: (response) => {  // Use an arrow function to maintain the correct context
            //         self.paged_books = response.paged_books;
            //         self.has_previous = response.has_previous;
            //         self.has_next = response.has_next;
            //         self.previous_page_number = response.previous_page_number
            //         self.next_page_number = response.next_page_number
            //     },
            //     error: function(err) {
            //         console.log('Error occurred when fetching page ', err);
            //     }
            // });
        },
    },
    created() {
        $.ajax({
            type: 'GET',
            url: `${window.location.href}`,
            success: (response) => { 
                const self = this
                const books = self.$refs.books
                const pagination = self.$refs.pagination
                const spinner = self.$refs.loader

                books.classList.add('d-none')
                pagination.classList.add('d-none')
                setTimeout(() => {
                    books.classList.remove('d-none')
                    pagination.classList.remove('d-none')
                    spinner.classList.add('d-none')
                }, 3000);
            },
            error: function(err) {
                console.log('Error occurred when fetch data', err);
            }
        });
    }
});
