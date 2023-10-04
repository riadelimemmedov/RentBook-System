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
            e.preventDefault();
            const self = this; // Store a reference to the Vue instance
            let url = null
            
            if(e.target.getAttribute('data-type') == 'next'){
                console.log('Next')
            }
            else if(e.target.getAttribute('data-type') == 'prev'){
                url = `${e.target.href}${this.previous_page_number=1}`
                console.log('Previous url ', url)
                console.log('Prev')
            }

            $.ajax({
                type: 'GET',
                url: e.target.href,
                success: (response) => {  // Use an arrow function to maintain the correct context
                    self.paged_books = response.paged_books;
                    self.has_previous = response.has_previous;
                    self.has_next = response.has_next;
                    self.previous_page_number = response.previous_page_number
                    self.next_page_number = response.next_page_number
                },
                error: function(err) {
                    console.log('Error occurred when fetching page ', err);
                }
            });
        },
    },
    created() {
        this.has_previous=false 
        this.has_next=true
        this.previous_page_number=1
    }
});
