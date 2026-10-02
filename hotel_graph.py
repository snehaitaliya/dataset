import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("hotel_booking.csv")
#---------------bar (room type)----------------

# sns.countplot(data=df,x="Room_Type")
# plt.xlabel("Room type")
# plt.ylabel("Number of Booking")
# plt.title("Booking By Room type ")
# plt.show()


#---------------pie (payment method)------------

# payment=df["Payment_Method"].value_counts()

# plt.pie(payment,labels=payment.index,autopct="%.2f%%")
# plt.title("Payment Method")
# plt.show()


#-----------------bar (city wise)------------------

# city=df["City"].value_counts()

# plt.figure(figsize=(11,5))
# sns.barplot(x=city.index,y=city.values)
# plt.title("Bookings by City")
# plt.xlabel("City")
# plt.ylabel("Bookings")
# plt.show()


#---------------histo(rating)-----------------

# sns.histplot(data=df,x="Rating")

# plt.title("Customer Rating Distribution")
# plt.xlabel("Rating")
# plt.ylabel("Number of Customers")
# plt.show()


#---------------pie (booking status)-----------

# status=df["Booking_Status"].value_counts()

# plt.pie(status,labels=status.index,autopct="%.2f%%")
# plt.title("Booking Status")
# plt.show()


#---------------heatmap---------------

# data=df.select_dtypes(include="number")

# plt.figure(figsize=(10,6))
# sns.heatmap(data.corr(),annot=True,cmap="coolwarm")
# plt.title("Hotel Booking Correlation")
# plt.show()


#----------------pie (gender)--------------

# gender=df["Gender"].value_counts()

# plt.pie(gender,labels=gender.index,autopct="%.2f%%")
# plt.title("Booking By Gender")
# plt.show()


#--------------scatter (nights vs total_am)-------------
# sns.scatterplot(data=df,x="Nights",y="Total_Amount")

# plt.title("Nights vs Total Amount")
# plt.xlabel("Number of Nights")
# plt.ylabel("Total Amount")
# plt.show()


#----------------bar(night vs total_am)----------------
# sns.barplot(data=df, x="Nights", y="Total_Amount")

# plt.title("Nights vs Total Amount")
# plt.xlabel("Number of Nights")
# plt.ylabel("Total Amount")
# plt.show()


#---------------histo(night vs total_am)----------------
# sns.histplot(data=df, x="Nights", y="Total_Amount")

# plt.title("Nights vs Total Amount")
# plt.xlabel("Number of Nights")
# plt.ylabel("Total Amount")
# plt.show()


