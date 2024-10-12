import kue from 'kue';

const push_notification_code = kue.createQueue();

const data = {
  phoneNumber: '46576890',
  message: 'message',
}

const push_notification = push_notification_code.create(
  'push_notification', data)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${push_notification.id}`);
    }
  })


push_notification.on('completed', () => {
  console.log('Notification job completed');
});

push_notification.on('failed', () => {
  console.log('Notification job failed');
});
