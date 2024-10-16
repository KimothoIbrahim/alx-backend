import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];


const push_notification_code_2 = kue.createQueue();


jobs.forEach((message) => {
  const job = push_notification_code_2.create('messages', message);

job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`); 
  }
})
})

push_notification_code_2.on('job complete', (id) => {
  console.log(`Notification job ${id} completed`);
})

push_notification_code_2.on('job failed', (id, err) => {
  console.log(`Notification job ${id} failed: ${err}`);
})

push_notification_code_2.on('job progress', (id, progress) => {
  console.log(`Notification job ${id} ${progress}% complete`);
})
