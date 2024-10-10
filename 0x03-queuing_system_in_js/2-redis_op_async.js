import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => console.log('Redis client connected to the server'));

const asyncGet = promisify(client.get).bind(client);
const asyncSet = promisify(client.set).bind(client);

try {
  const setNewSchool = async (schoolName, value) => {
    await asyncSet(schoolName, value);
    console.log('Reply: OK');
}

  const displaySchoolValue = async (schoolName) => {
    const outcome =  await asyncGet(schoolName);
    console.log(outcome);
  }

  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');

} catch (err) {
  console.log(err);
}

