from django.shortcuts import render

def live_stream(request):
    # This must be the exact IP of your Pi
    pi_ip_address = '192.168.1.7'  
    # This must be the exact port of your Flask app
    pi_port = 5000
    context = {
        'pi_ip': pi_ip_address,
        'pi_port': pi_port,
    }
    return render(request, 'camera_stream/live_stream.html', context)