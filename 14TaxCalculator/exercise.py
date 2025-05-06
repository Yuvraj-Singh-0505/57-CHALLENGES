order_amount = float(input("What is the order amount? "))

gst_rate = 0.18

gst = order_amount * gst_rate

print("GST: ₹" + str(round(gst, 2)))
