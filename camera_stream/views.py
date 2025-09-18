from django.shortcuts import render

def live_stream(request):
    """
    Renders the HTML template that displays the live video stream from the Raspberry Pi.
    """
    # Replace with the actual IP address of your Raspberry Pi.
    # You can find this by running `hostname -I` on your Pi.
    pi_ip_address = '192.168.1.7'
    
    # This is the port your Flask app is running on.
    pi_port = 5000
    
    context = {
        'pi_ip': pi_ip_address,
        'pi_port': pi_port,
    }
    
    # Renders the live_stream.html template with the Pi's IP and port.
    return render(request, 'camera_stream/live_stream.html', context)