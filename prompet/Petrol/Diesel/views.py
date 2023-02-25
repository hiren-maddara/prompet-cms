from .forms import form1
from .models import Diese

# from .forms import form2
from django.views.generic import FormView

# Create your views here.
class DieselView(FormView):
   form_class = form1
   template_name = "Diesel/listing.html"
   success_url = "/Diesel/listing/"

   def form_valid(self,form):
      """Process and Save to DB when form is valid"""
      customer_name = form.cleaned_data["Customername"]
      telephone_contact = form.cleaned_data["Telephonecontact"]
      date = form.cleaned_data["Date"]
      employee_name = form.cleaned_data["EmployeeName"]
      employee_address = form.cleaned_data["EmployeeAddress"]
      fuel_type = form.cleaned_data["Fueltype"]
      amt_litres = form.cleaned_data["AmountinLitres"]
      unitprice = form.cleaned_data["UnitPrice"]
      total_price = form.cleaned_data["TotalPrice"]
      diesel_form = Diese(
            Customername=customer_name,
            Telephonecontact=telephone_contact,
            Date=date,
            EmployeeName=employee_name,
            EmployeeAddress=employee_address,
            Fueltype=fuel_type,
            AmountinLitres=amt_litres,
            UnitPrice=unitprice,
            TotalPrice=total_price,
      )
      diesel_form.save()
      # Redirect to the success URL above
      return super().form_valid(form)

   def form_invalid(self,form):
      # Render the form with validation errors
      return self.render_to_response(self.get_context_data(form=form))
