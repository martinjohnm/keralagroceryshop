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

    } else if (type === 'auto-close') {
      swal({
        title: 'Auto close alert!',
        text: 'I will close in 2 seconds.',
        timer: 2000,
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
    } else if (type === 'warning-message-and-cancel') {
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
    
    } else if (type === 'unblock-customer') {
      swal({
        title: 'Are you sure?',
        text: "You really want to unblock the customer",
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
          window.location = "/Admin/unBlockCustomer/?id=" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    } else if (type === 'delete-product') {
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
          
          window.location = "/delete_product_cart/" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    } else if (type === 'delete-categoryOffer') {
      swal({
        title: 'Are you sure?',
        text: "You really want to delete this Category Offer?",
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
          const id = document.getElementById('id').value
          window.location = "/Admin/deleteCategoryOffer/?offer_id=" + id ;
        } 
        // window.location = "redirectURL";
    });
    
    }

    else if (type === 'delete-cart') {
    swal({
      title: 'Are you sure?',
      text: "You really want to delete Cart?",
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
      console.log(data)
      if(data === true)
       {
        window.location = "/delete_cart";
       } 

      // if(data === true){
      //   const id = document.getElementById('id').value
        
      // } 
      // window.location = "redirectURL";
  });
  
  }
  else if (type === 'delete-cart-session') {
    swal({
      title: 'Are you sure?',
      text: "You really want to delete Cart?",
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
      console.log(data)
      if(data === true)
       {
        window.location = "/delete_cart";
       } 

      // if(data === true){
      //   const id = document.getElementById('id').value
        
      // } 
      // window.location = "redirectURL";
  });
  
  }
  
  
  // else if (type === 'add_cart') {
  //   swal({
  //     title: 'Item Adde to cart',
  //     // text: 'You entered the correct answer',
  //     icon: 'success',
  //     button: {
  //       text: "Continue",
  //       value: true,
  //       visible: true,
  //       className: "btn btn-primary"
  //     }
  //   })

  // }

  else if (type === 'add_cart') {
    swal({
      title: 'Item Adde to cart!',
      //text: 'I will close in 2 seconds.',
      timer: 700,
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
   else if (type === 'return_order') {
    swal({
      title: 'Are you sure?',
      text: "You really want to Return order ?",
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
      const id = document.getElementById('return_data').value
        window.location = "/return_order/" + id ;

      // if(data === true){
      //   const id = document.getElementById('id').value
        
      // } 
      // window.location = "redirectURL";
  });
  
  }
  
  

  else if (type === 'return-order') {
    console.log('rir');
    swal({
      
      title: 'Are you sure?',
      text: "You really want to Return this order ?",
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
      console.log('hi');
      if(data === true){
        
        window.location = "/return_order/" + id ;
      } 
      

      // if(data === true){
      //   const id = document.getElementById('id').value
        
      // } 
      // window.location = "redirectURL";
  });
  
  }

  
  else if (type === 'cancel-user-order') {
    console.log('rir');
    swal({
      
      title: 'Are you sure?',
      text: "You really want to Cancel this order ?",
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
      console.log('hi');
      if(data === true){
        
        window.location = "/order_cancel_user/" + id ;
      } 
     
  });
  
  }
  else if (type === 'delete-address') {
    console.log('rir');
    swal({
      
      title: 'Are you sure?',
      text: "You really want to delete this address ?",
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
      console.log('hi');
      if(data === true){
        
        window.location = "/delete_address_user/" + id ;
      } 
     
  });
  
  }
  
  } 
})(jQuery);


