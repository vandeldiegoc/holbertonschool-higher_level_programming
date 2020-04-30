listint_t *insert_node(listint_t **head, int number)
{
    listint_t *newnode, *ptr = *head;
    if (head == NULL)
		return (NULL);

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    if (*head == NULL)
    {
        *head = new; 
        new->next = NULL;
        return (new);
    }

