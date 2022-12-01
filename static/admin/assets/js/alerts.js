(function($) {
  showSwal = function(type,id) {
    'use strict';
    if (type === 'basic') {
      swal({
        text: 'Any fool can use a computer',
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'title-and-text') {
      swal({
        title: 'Read the alert!',
        text: 'Click OK to close this alert',
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'success-message') {
      swal({
        title: 'Congratulations!',
        text: 'You entered the correct answer',
        icon: 'success',
        button: {
          text: "Continue",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'add-category-offer') {
      swal({
        title: 'Category offer added!',
        text: '',
        timer: 10000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    }
    else if (type === 'update-category-offer') {
      swal({
        title: 'Category offer updated!',
        text: '',
        timer: 10000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    }
    else if (type === 'update-product-offer') {
      swal({
        title: 'Product offer Updated!',
        text: '',
        timer: 10000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    }
    else if (type === 'add-product-offer') {
      swal({
        title: 'Product offer Added!',
        text: '',
        timer: 10000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    }
    else if (type === 'update_coupon') {
      swal({
        title: 'Coupon Updated!',
        text: '',
        timer: 10000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    }
    else if (type === 'add_coupon') {
      swal({
        title: 'Coupon Added!',
        text: '',
        timer: 10000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    }
    
    
     else if (type === 'warning-message-and-cancel') {
      swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        console.log()
        if(data === true){
          const id = document.getElementById('category_id').value
          window.location = "/Admin/deleteCategory/?id=" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    } else if (type === 'custom-html') {
      swal({
        content: {
          element: "input",
          attributes: {
            placeholder: "Type your password",
            type: "password",
            class: 'form-control'
          },
        },
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })
    } else if (type === 'block-customer') {
      swal({
        title: 'Are you sure?',
        text: "You really want to block the customer",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        console.log()
        if(data === true){
          const id = document.getElementById('customer_id').value
          window.location = "/Admin/BlockCustomer/?id=" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    }  else if (type === 'delete-product') {
      swal({
        title: 'Are you sure?',
        text: "You really want to delete the product",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/delete_product/" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    } else if (type === 'delete-category') {
      swal({
        title: 'Are you sure?',
        text: "You really want to delete this Category ?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/delete_category/" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    } else if (type === 'reject_order') {
      swal({
        
        title: 'Are you sure?',
        text: "You really want to reject the order",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          const id = document.getElementById('reject_order').value
          window.location = "/order_reject/" + id ;
        } 
        // window.location = "redirectURL";
    });
    }
    
    else if (type === 'accept_order') {
      swal({
        title: 'Are you sure?',
        text: "You really want to accept this order?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
         
          window.location = "/order_accept/" + id ;
        } 
        
    });}
    


    else if (type === 'block_user') {
      swal({
        title: 'Are you sure?',
        text: "You really want to block?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/block/" + id ;
          // href="/block/{{ item.id }}"
        } 
        
  
        // if(data === true){
        //   const id = document.getElementById('id').value
          
        // } 
        // window.location = "redirectURL";
    });}
    else if (type === 'unblock_user') {
      swal({
        title: 'Are you sure?',
        text: "You really want to unblock?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/unblock/" + id ;
          // href="/block/{{ item.id }}"
        } 
        
  
        // if(data === true){
        //   const id = document.getElementById('id').value
          
        // } 
        // window.location = "redirectURL";
    });}

    else if (type === 'order_cancel') {
      swal({
        title: 'Are you sure?',
        text: "You really want to cancel the order",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          const id = document.getElementById('order_cancel').value
          window.location = "/order_cancel_user/" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    }

    else if (type === 'delete_coupon') {
      swal({
        title: 'Are you sure?',
        text: "You really want to Delete this Coupon?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/delete_coupon/" + id ;
          // href="/block/{{ item.id }}"
        } 
        
  
        // if(data === true){
        //   const id = document.getElementById('id').value
          
        // } 
        // window.location = "redirectURL";
    });}
    
    else if (type === 'delete-product-offer') {
      swal({
        title: 'Are you sure?',
        text: "You really want to Delete this Offer?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/delete_product_offer/" + id ;
          // href="/block/{{ item.id }}"
        } 
        
    });}
    else if (type === 'delete-category-offer') {
      swal({
        title: 'Are you sure?',
        text: "You really want to Delete this Offer?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          }
        }
      }).then((data) => {
        if(data === true){
          
          window.location = "/delete_category_offer/" + id ;
          // href="/block/{{ item.id }}"
        } 
        
    });}
    
  } 
  
})(jQuery);



