import { format, parseISO } from 'date-fns'

const DATE_FORMAT = 'MMM d, yyyy'

export const formatDate = (isoString: string) =>
  format(parseISO(isoString), DATE_FORMAT)
