class IndexView(CoreIndexView):
    success_url = reverse_lazy('checkout:shipping-method')

class ShippingMethodView(CoreShippingMethodView):
    def post(self, request, *args, **kwargs):
        # Need to check that this code is valid for this user
        method_code = request.POST.get('method_code', None)
        if not self.is_valid_shipping_method(method_code):
            messages.error(request, _("Your submitted shipping method is not"
                                      " permitted"))
            return redirect('checkout:shipping-method')

        # Save the code for the chosen shipping method in the session
        # and continue to the next step.
        self.checkout_session.use_shipping_method(method_code)

        if method_code != 'self-pickup':
            return redirect('checkout:shipping-address')
        return self.get_success_response()

class ShippingAddressView(CoreShippingAddressView):
    success_url = reverse_lazy('checkout:payment-method')

    def post(self, request, *args, **kwargs):
        # Check if a shipping address was selected directly (eg no form was
        # filled in)
        if self.request.user.is_authenticated() \
                and 'address_id' in self.request.POST:
            address = UserAddress._default_manager.get(
                pk=self.request.POST['address_id'], user=self.request.user)
            action = self.request.POST.get('action', None)
            if action == 'ship_to':
                # User has selected a previous address to ship to

                # Получаем код способа доставки, чтобы после
                # сброса записать его снова
                method_code = self.checkout_session.shipping_method_code(
                    self.request.basket)
                self.checkout_session.ship_to_user_address(address)
                if method_code:
                    self.checkout_session.use_shipping_method(method_code)
                return redirect(self.get_success_url())
            else:
                return http.HttpResponseBadRequest()
        else:
            return super(ShippingAddressView, self).post(
                request, *args, **kwargs)