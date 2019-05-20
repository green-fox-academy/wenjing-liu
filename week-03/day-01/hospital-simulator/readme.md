### Hospital simulator

Now you are going to create a simple hospital simulator game. We will need
patients, a hospital and different kinds of queues to handle our patients.
You can implement the necessary classes in any order, but I suggest you to
follow the descriptions below.

#### Patient class

The *Patient* class doesn't depend on any other classes.
It has two methods:

- One to retrieve the severity of the disease.
- One to treat the patient, it must decrease the severity by 1.

The severity is a random number between 1 and 10, you can set it in the
constructor or at the field declaration.
*Keep in mind, the severity cannot go below 0*

#### Queue class

If you have *Patient*s you can create an abstract *Queue* class. It will hold
the patients waiting for treatment.

- It should have a method to add *Patient*s to the queue.
- It should have an abstract method to get the next patient.

The implementation is up to you, you can store the patients in any data structure.

#### Hospital class

Since you have *Queue* class and *Patient*s you can implement your *Hospital*
class as well. Which must fulfill the following requirements:

- It has a *Queue* which is set through the constructor.
- It has a method to add a *Patient* to the queue.
- It has a method to treat the next patient in the queue.

#### SafeQueue class

The safe queue is a special queue which is not abstract anymore. Its method
to retrieve the next patient has the following specification

- It always returns the patient with the highest severity.
- If there are more patients with the same severity you can pick one, it is up to
  you which one is returned.
- Patients with 0 severity can be skipped or removed from the queue.
- You can return `null` if all the patients have 0 severity or the queue is empty

#### ClassicQueue class

The classic queue is a special queue which is not abstract anymore. Its method
to retrieve the next patient has the following specification

- It should return always the next patient. (You need to track who was the
  last treated patient.)
- It should handle the cycles, so after the last patient it must return the
  first one again.
- Patients with 0 severity won't be returned ever. (You can remove them from the
  queue or just simple skip them)
- You can return `null` if all the patients have 0 severity or the queue is empty