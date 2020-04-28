#include "lists.h"
/**
 * check_cycle -  checks if a singly linked list has a cycle in it.
 * @list: nodos
 * Return: 0 it's not cycle, 1 it's cycle
 */
int check_cycle(listint_t *list)
{
listint_t *nodo = list;
listint_t *nodon = list;
while (nodo && nodon && nodon->next)
{
nodo = nodo->next;
nodon = nodon->next->next;
if (nodo == nodon)
return (1);
}
return (0);
}
