#include "lists.h"
/**
 * check_cycle - a function that checks if a linked list has a recurring cycle
 * list: a pointer to the linked list in question
 *Return: 1 if a cycle is found and 0 if a failure is not found
 */
int check_cycle(listint_t *list)
{
  listint_t *current;
  listint_t *power;

  current = list;
  power = list;

  while (current != NULL)
  {
    current = current->next;

    if (current == power)
      return (1);
  }
  return (0);
}
    
    
      
