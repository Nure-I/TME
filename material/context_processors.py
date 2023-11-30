from .models import Course , Topic # Import your model if needed

def common_data(request):
    # Add your data to the dictionary
    courseId = request.GET.get('courseId')
    topicId = request.GET.get('topicId')
    if topicId:
      topics = Topic.objects.filter(course__id= courseId)
      
    
    topics = Topic.objects.filter(course__id= courseId)
    common_data_dict = {
        'courses': Course.objects.all(),  # Example: Pass instances of YourModel
        'topics': topics

    }

    return common_data_dict