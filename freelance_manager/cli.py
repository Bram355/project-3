import typer
from datetime import date
from freelance_manager.database import SessionLocal, engine
from freelance_manager.models import Client, Project, Invoice, Payment, INVOICE_STATUSES

app = typer.Typer()

@app.command()
def init_db():
    from freelance_manager.database import Base
    Base.metadata.create_all(bind=engine)
    typer.echo("Database initialized.")

# CLIENT COMMANDS

@app.command()
@app.command()
def add_client(
    name: str = typer.Option(..., help="Client's name"),
    email: str = typer.Option(..., help="Client's email"),
):
    db = SessionLocal()
    client = Client(name=name, email=email)
    db.add(client)
    db.commit()
    typer.echo(f"Added client: {name} ({email})")


@app.command()
def list_clients():
    db = SessionLocal()
    clients = db.query(Client).all()
    for client in clients:
        typer.echo(f"ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone: {client.phone}")

# PROJECT COMMANDS

@app.command()
def add_project(
    client_id: int, 
    name: str, 
    description: str = "", 
    start_date: str = None, 
    end_date: str = None
):
    db = SessionLocal()
    project = Project(
        name=name,
        description=description,
        client_id=client_id,
        start_date=date.fromisoformat(start_date) if start_date else None,
        end_date=date.fromisoformat(end_date) if end_date else None,
    )
    db.add(project)
    db.commit()
    typer.echo(f"Added project: {name} for client ID {client_id}")

@app.command()
def list_projects():
    db = SessionLocal()
    projects = db.query(Project).all()
    for project in projects:
        typer.echo(f"ID: {project.id}, Name: {project.name}, Client ID: {project.client_id}")

# INVOICE COMMANDS

@app.command()
def add_invoice(
    project_id: int, 
    amount: float, 
    due_date: str, 
    status: str
):
    if status not in INVOICE_STATUSES:
        typer.echo(f"Invalid status. Must be one of {INVOICE_STATUSES}")
        raise typer.Exit()

    db = SessionLocal()
    invoice = Invoice(
        project_id=project_id,
        amount=amount,
        due_date=date.fromisoformat(due_date),
        status=status
    )
    db.add(invoice)
    db.commit()
    typer.echo(f"Added invoice for project ID {project_id}")

@app.command()
def list_invoices():
    db = SessionLocal()
    invoices = db.query(Invoice).all()
    for invoice in invoices:
        typer.echo(f"ID: {invoice.id}, Project ID: {invoice.project_id}, Amount: {invoice.amount}, Status: {invoice.status}")

# PAYMENT COMMANDS

@app.command()
def add_payment(
    invoice_id: int,
    amount: float,
    payment_date: str
):
    db = SessionLocal()
    payment = Payment(
        invoice_id=invoice_id,
        amount=amount,
        payment_date=date.fromisoformat(payment_date),
    )
    db.add(payment)
    db.commit()
    typer.echo(f"Added payment of {amount} for invoice ID {invoice_id}")

@app.command()
def list_payments():
    db = SessionLocal()
    payments = db.query(Payment).all()
    for payment in payments:
        typer.echo(f"ID: {payment.id}, Invoice ID: {payment.invoice_id}, Amount: {payment.amount}, Date: {payment.payment_date}")

if __name__ == "__main__":
    app()
