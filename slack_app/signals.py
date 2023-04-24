from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.shortcuts import render,HttpResponse
from django.core.management import call_command
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from io import StringIO
from django.core.management.commands.makemigrations import Command
from slackeventsapi import SlackEventAdapter 
import slack_sdk


# @slack_event_adapter.on('message')
@receiver(post_migrate)
def my_callback(sender, **kwargs):
    client = WebClient(token="xoxb-2023650115936-5034118136742-4oETG6XZVPUL1goxq4hZd12T")
    channel_id = 'U03HEU9JBAA'
    try:
        # import pdb;pdb.set_trace()
        message=[]
        if kwargs['plan']:
          for detail in kwargs['plan']:
            migration_detail=detail[0]
            app_name=migration_detail.app_label
            migration_operation_detail=migration_detail.operations
            for operation_detail in migration_operation_detail:
                
                if operation_detail.__class__.__name__=="AddField":
                  print("add Field")
                  message.append("Field:-%s_%s_%s__%s" % (app_name,operation_detail.model_name,operation_detail.name,operation_detail.__class__.__name__))

                if operation_detail.__class__.__name__=="RemoveField":
                  print('remove field')
                  message.append("Field:-%s_%s_%s__%s" % (app_name,operation_detail.model_name,operation_detail.name,operation_detail.__class__.__name__))

                if operation_detail.__class__.__name__=="RenameField":
                  print('rename field')
                  message.append("Field:-%s_%s_%s to %s__%s" % (app_name,operation_detail.model_name,operation_detail.old_name,operation_detail.new_name,operation_detail.__class__.__name__))
                  print(message)

                if operation_detail.__class__.__name__=="CreateModel":
                      print('create table')
                      message.append("Table:-%s_%s__%s" % (app_name,operation_detail.name,operation_detail.__class__.__name__))

                if operation_detail.__class__.__name__=="RenameModel":
                  print('rename table')
                  message.append("Table:-%s_%s to %s__%s" % (app_name,operation_detail.old_name,operation_detail.new_name,operation_detail.__class__.__name__))

                if operation_detail.__class__.__name__=="DeleteModel":
                  print('Delete table')
                  message.append("Table:-%s_%s__%s" % (app_name,operation_detail.name,operation_detail.__class__.__name__))
  
            break
          response = client.chat_postMessage(channel=channel_id, text='\n'.join(message))
          print(response)
    except SlackApiError as e:
        print("Error sending message: ", e)
    # return HttpResponse('Done')